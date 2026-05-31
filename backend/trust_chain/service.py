from backend.crypto.signing import (
    sign_message,
    verify_message
)


def build_trust_chain(
    finding,
    research_agent,
    review_agent,
    security_agent
):

    # Stage 1
    research_signature = sign_message(
        finding,
        research_agent.private_key
    )

    research_verified = verify_message(
        finding,
        research_signature,
        research_agent.public_key
    )

    # Stage 2
    review_payload = (
        f"{finding}|{research_signature}"
    )

    review_signature = sign_message(
        review_payload,
        review_agent.private_key
    )

    review_verified = verify_message(
        review_payload,
        review_signature,
        review_agent.public_key
    )

    # Stage 3
    security_payload = (
        f"{finding}|"
        f"{research_signature}|"
        f"{review_signature}"
    )

    security_signature = sign_message(
        security_payload,
        security_agent.private_key
    )

    security_verified = verify_message(
        security_payload,
        security_signature,
        security_agent.public_key
    )

    return {

        "finding": finding,

        "research_agent": research_agent.name,
        "review_agent": review_agent.name,
        "security_agent": security_agent.name,

        "research_signature": research_signature,
        "review_signature": review_signature,
        "security_signature": security_signature,

        "research_verified": research_verified,
        "review_verified": review_verified,
        "security_verified": security_verified,

        "chain_valid": (
            research_verified
            and review_verified
            and security_verified
        )
    }