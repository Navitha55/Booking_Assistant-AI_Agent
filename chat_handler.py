from Backend.langgraph_agent import run_langgraph_flow
from Backend.calendar_utils import check_availability, create_event

async def handle_user_message(message: str) -> str:
    try:
        response = run_langgraph_flow(message)
        intent = response.get("intent")
        if intent == "book":
            if "datetime" in response and "start" in response and "end" in response and "summary" in response:
                available = check_availability(response["datetime"])
                if available:
                    create_event(response["summary"], response["start"], response["end"])
                    return "✅ Your meeting is booked!"
                else:
                    return "❌ No available slots at that time."
            else:
                return "⚠️ Sorry, I couldn't extract complete date/time details."
        elif intent == "cancel":
            return "🔄 Canceling meetings is not implemented yet."
        
        elif intent == "reschedule":
            return "🔁 Rescheduling meetings is not implemented yet."
        else:
            return response.get("text", "🤖 I couldn't understand that. Could you try rephrasing?")

    except Exception as e:
        return f"❌ An error occurred: {str(e)}"
