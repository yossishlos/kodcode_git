import json

data = "soldiers.json"

def get_soldiers():
    with open(data, "r", encoding="utf-8")as file:
        return json.load(file)
    
def get_soldier_by_id(id: int):
    with open(data, "r", encoding="utf-8")as file:
        db = json.load(file)
        for soldier in db:
            if soldier["id"] == id:
                return soldier
            
def add_soldier(new_soldier: dict):
    soldiers = get_soldiers()
    for soldier in soldiers:
        if soldier["id"] == new_soldier["id"]:
            return
        
    soldiers.append(new_soldier)
    with open(data, "w", encoding="utf-8") as file:
        json.dump(soldiers, file, indent=4)
    
    return {"message": "good"}

def update_soldier(id: int, new_data: dict):
    soldiers = get_soldiers()
    for soldier in soldiers:
        if soldier["id"] == id:
            
            soldier.update(new_data)

            with open(data, "w", encoding="utf-8") as file:
                json.dump(soldiers, file, indent=4)
            return {"message": "very good"}
        
    return {"message": "soldier not found"}