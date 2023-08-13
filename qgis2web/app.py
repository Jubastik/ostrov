import asyncio
import logging

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from asyncio import sleep
import requests
from os import getenv

from template import base_plate, camp_plate
from copy import deepcopy

load_dotenv()


async def map_updater():
    while True:
        try:
            f_data = deepcopy(base_plate)
            camps = requests.get(f"{getenv('API_URL')}api/camp").json()
            for ind, camp in enumerate(camps):
                camp_detail = requests.get(f"{getenv('API_URL')}api/camp_detail/{camp['id']}").json()
                print(camp_detail)
                if len(camp_detail) == 0:
                    continue

                f_camp = deepcopy(camp_plate)
                f_camp["geometry"]["coordinates"] = [camp["longitude"], camp["latitude"]]

                f_camp["properties"] = {"fid": ind + 1,
                                        "Название стоянки": camp["name"],
                                        "Занятость": camp["occupation"],
                                        "Температура": camp["temperature"],
                                        "Влажность": camp["humidity"],
                                        "Давление": camp["pressure"],
                                        "Видимость с воды": camp_detail["visibility"],
                                        "Выход на берег": camp_detail["ashore"],
                                        "Число палаток": camp_detail["number_tents"],
                                        "Дрова": camp_detail["firewood"],
                                        "Связь": camp_detail["connection"],
                                        "Наличие комаров": camp_detail["mosquitoes"],
                                        "Достопримечательности": camp_detail["attractions"],
                                        "Удобства": camp_detail["conveniences"],
                                        "Размер": camp_detail["size"],
                                        "Виды на закаты/рассветы": camp_detail["sunset"],
                                        "Дополнительно": camp_detail["description"],
                                        }
                f_data["features"].append(f_camp)
            with open("static/data/_9.js", mode="w", encoding="UTF8") as file:
                file.write(f"var json__9 = {f_data}")

            await sleep(30)
        except Exception as e:
            logging.error(f"Ошибка API: {e}")
            await sleep(60)


async def on_start():
    asyncio.create_task(map_updater())


app = FastAPI(on_startup=[on_start], title="app app")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
