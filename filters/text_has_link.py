from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message


class HasLinkFilter(BaseFilter):
     async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
         # If there are no entities at all, None will be returned,
         # in this case we assume that this is an empty list
         entities = message.entities or []

         # If there is at least one link, return it
         for entities in entities:
             if entity.type == "url":
                 return {"link": entity.extract_from(message.text)}

         # If nothing is found, return None
         return False