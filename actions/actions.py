# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .latex_list import bullets, simple_headline, numbers
from .paper_search import paper_search


class ActionUtterList(Action):

    def name(self) -> Text:
        return "action_utter_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        all_headlines = tracker.get_slot("list")
        chunks = all_headlines.split(',')

        list_type = tracker.get_slot("category_list")

        if "bullets" in list_type:
            dispatcher.utter_message(text= bullets(chunks))
        elif "numbers" in list_type:
            dispatcher.utter_message(text=numbers(chunks))        
        elif "headline" in list_type:
            dispatcher.utter_message(text=simple_headline(chunks))
        return [AllSlotsReset()]

class ActionUtterPaper(Action):

    def name(self) -> Text:
        return "action_utter_paper"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #topic = tracker.get_slot("paper")
        #result = paper_search(topic)

        dispatcher.utter_message(text=tracker.get_slot("paper"))
        return [AllSlotsReset()]

class ValidatePaperForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_paper_form"

    @staticmethod
    def category_list() -> List[Text]:
        """Database of supported categories"""

        return ["numbers", "bullets", "simple headlines"]

    def validate_paper(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate category value."""

        topic = tracker.get_slot("paper")
        result = paper_search(topic)
        if not result:
            final_string = "Sorry I couldn't find any results for your request. Please repeat the topic you want more information about."
            dispatcher.utter_message(text=final_string)
            dispatcher.utter_message(text=" ")
            return {"paper": None}
        else:
            return {"paper": result}
 

class ValidateListForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_list_form"

    @staticmethod
    def category_list() -> List[Text]:
        """Database of supported categories"""

        return ["numbers", "bullets", "simple headlines"]

    def validate_category_list(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate category value."""

        if slot_value.lower() in self.category_list():
            return {"category_list": slot_value}
        else:
            dispatcher.utter_message(text="I didn't get your list type.")
            dispatcher.utter_message(text=" ")
            return {"category_list": None}
 