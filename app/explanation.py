import pandas as pd
import streamlit as st

from data.config import thresholds


def get_factor_level(feature, value):
    """Return a display-only contextual range for an entered patient value."""
    if feature == "Glucose":
        return "Low" if value < 70 else "Typical" if value < 140 else "High"
    if feature == "BMI":
        return "Low" if value < 18.5 else "Typical" if value < 25 else "Moderate" if value < 30 else "High"
    if feature == "Age":
        return "Low" if value < 30 else "Moderate" if value < 45 else "High"
    if feature == "Insulin":
        return "Low" if value < 30 else "Typical" if value < 200 else "High"
    if feature == "Pregnancies":
        return "Low" if value <= 2 else "Moderate" if value <= 5 else "High"
    raise ValueError(f"Unsupported factor: {feature}")


def _format_factor_names(factors):
    if len(factors) == 1:
        return factors[0].lower()
    if len(factors) == 2:
        return f"{factors[0].lower()} and {factors[1].lower()}"
    return f"{', '.join(factor.lower() for factor in factors[:-1])}, and {factors[-1].lower()}"


def _build_summary(factor_rows, prediction_probability):
    risk_label = "Diabetes Risk" if prediction_probability >= thresholds else "No Diabetes"
    higher_factors = [row["Factor"] for row in factor_rows if row["Level"] == "High"]
    moderate_factors = [row["Factor"] for row in factor_rows if row["Level"] == "Moderate"]

    if higher_factors:
        summary = (
            f"Your prediction was classified as {risk_label}. Among the entered parameters, "
            f"{_format_factor_names(higher_factors)} {'is' if len(higher_factors) == 1 else 'are'} "
            "in higher contextual ranges"
        )
        if moderate_factors:
            summary += (
                f", while {_format_factor_names(moderate_factors)} "
                f"{'is' if len(moderate_factors) == 1 else 'are'} in a moderate range"
            )
        return summary + "."

    lower_or_typical_count = sum(row["Level"] in {"Low", "Typical"} for row in factor_rows)
    if risk_label == "No Diabetes" and lower_or_typical_count >= 3:
        return "Your prediction was classified as No Diabetes. Most entered parameters are within lower or typical contextual ranges."

    if moderate_factors:
        return (
            f"Your prediction was classified as {risk_label}. "
            f"{_format_factor_names(moderate_factors).capitalize()} {'is' if len(moderate_factors) == 1 else 'are'} "
            "in a moderate contextual range, while the other entered parameters are lower or typical."
        )

    return f"Your prediction was classified as {risk_label}. The entered parameters are within lower or typical contextual ranges."


def app(input_data, prediction_probability):
    """Render value-range context separate from the machine-learning prediction."""
    factor_order = ["Glucose", "BMI", "Age", "Insulin", "Pregnancies"]
    factor_rows = []
    for feature in factor_order:
        value = float(input_data.iloc[0][feature])
        # These fixed ranges describe entered values only, not ML feature attributions.
        factor_rows.append({
            "Factor": feature,
            "Patient Value": int(value) if value.is_integer() else value,
            "Level": get_factor_level(feature, value),
        })

    st.markdown("### Why This Prediction?")
    st.markdown("#### Key Patient Factors")
    st.markdown("The following summarizes the health parameters entered for this prediction.")
    st.dataframe(pd.DataFrame(factor_rows), hide_index=True, use_container_width=True)
    st.caption(
        "Display-only contextual ranges: Glucose <70 low, 70–139 typical, ≥140 high; "
        "BMI <18.5 low, 18.5–24.9 typical, 25–29.9 moderate, ≥30 high; "
        "Age <30 low, 30–44 moderate, ≥45 high; Insulin <30 low, 30–199 typical, ≥200 high; "
        "Pregnancies 0–2 low, 3–5 moderate, ≥6 high."
    )
    st.markdown(_build_summary(factor_rows, prediction_probability))
    st.caption(
        "These labels provide context for the entered values only. They are not model feature contributions, "
        "causal effects, or a diagnosis."
    )
