from fastapi import APIRouter, Request
import json

router = APIRouter()

@router.get("/api/setting")
def read_setting():
    f = open('setting.json', 'r')
    setting = json.load(f)
    return setting