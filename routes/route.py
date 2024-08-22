from fastapi import APIRouter
from models.todos import Todo
from config.database import col
from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()


# GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(col.find())
    return todos


# POST request method
@router.post("/")
async def post_todo(todo: Todo):
    col.insert_one(dict(todo))
    return todo


# PUT request method
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    col.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return todo


# DELETE request method
@router.delete("/{id}")
async def delete_todo(id: str):
    col.find_one_and_delete({"_id": ObjectId(id)})
    return "Deleted successfully"
