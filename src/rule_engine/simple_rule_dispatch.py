# Simple rule engine that dispatches actions based on predicates using a list of rules

from dataclasses import dataclass


@dataclass
class RuleItem:
    condition: callable
    operation: callable


def execute_rules(rule_list, context):
    for rule in rule_list:
        if rule.condition(context):
            return rule.operation(context)
    return None


# Example usage
my_rules = [
    RuleItem(lambda ctx: ctx["state"] == "initial", lambda ctx: "initialize"),
    RuleItem(lambda ctx: ctx["state"] == "error", lambda ctx: "recover"),
    RuleItem(lambda ctx: ctx["level"] > 3, lambda ctx: "alert"),
]
print(execute_rules(my_rules, {"state": "initial"}))  # Outputs: "initialize"
