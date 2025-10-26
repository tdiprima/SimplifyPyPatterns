# Old way using nested if statements for conditional logic


def handle_context(context):
    if context["state"] == "initial":
        return "initialize"
    elif context["state"] == "error":
        return "recover"
    elif context["level"] > 3:
        return "alert"
    return None


# Example usage
print(handle_context({"state": "initial"}))  # Outputs: "initialize"
