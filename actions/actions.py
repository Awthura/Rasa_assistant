from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from typing import Text, Dict, List, Any
from rasa_sdk import utils

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data.json")
        super().__init__(knowledge_base)

    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ):
        """
        Utters a response to the user that lists all found objects.
        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if objects:
            dispatcher.utter_message(
                text=f"Found the following objects of type '{object_type}':"
            )

            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )

            num_items = 3 #adjustable
            for i, obj in enumerate(objects[:num_items], 1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"I could not find any objects of type '{object_type}'."
            )
