ROLE_POLICIES = {

    "research": [
        "web_search",
        "repository_scan"
    ],

    "security": [
        "approve_report",
        "view_audit_log"
    ],

    "review": [
        "code_review"
    ]
}


def is_action_allowed(
    role: str,
    action: str
):

    allowed_actions = ROLE_POLICIES.get(
        role,
        []
    )

    return action in allowed_actions