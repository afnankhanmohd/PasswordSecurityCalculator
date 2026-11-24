
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    formula = ""
    strength = ""
    total_characters = 0

    if request.method == "POST":

        password_type = request.form.get("type")
        length = int(request.form.get("length", 0))

        if length < 1 or length > 30:
            result = "Please enter a length between 1 and 30."

        elif password_type == "pin":

            total_characters = 10
            formula = "10^" + str(length)
            result = total_characters ** length

        else:

            if request.form.get("lowercase"):
                total_characters += 26

            if request.form.get("uppercase"):
                total_characters += 26

            if request.form.get("numbers"):
                total_characters += 10

            if request.form.get("symbols"):
                total_characters += 32

            if total_characters == 0:
                result = "Please select at least one character type."

            else:
                formula = str(total_characters) + "^" + str(length)
                result = total_characters ** length

        if isinstance(result, int):

            if result < 1000000:
                strength = "Low number of possibilities"
            elif result < 1000000000000:
                strength = "Moderate number of possibilities"
            else:
                strength = "High number of possibilities"

    return render_template(
        "index.html",
        result=result,
        formula=formula,
        strength=strength
    )


if __name__ == "__main__":
    app.run(debug=True)
