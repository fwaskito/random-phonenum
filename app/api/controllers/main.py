from flask import request, session
from flask import render_template, flash, redirect, url_for
from app.forms import MainForm
from app.api import bp
from app.utils.generator import RandomNumberGenerator


@bp.route("/", methods=["GET", "POST"])
def main():
    header = "Header"
    if request.method == "GET":
        form = MainForm(request.form)
        return render_template("main.html", form=form, header=header, page="main")
    if request.method == "POST":
        form = MainForm(request.form)
        header = form.header.data
        duplication = float(form.duplication.data)
        quantity = form.quantity.data
        if quantity > 0:
            prefix = form.prefix.data
            generator = RandomNumberGenerator(quantity, prefix, duplication)
            generator.generate()
            numbers = generator.phone_numbers

            session["numbers"] = numbers
            session["distribution"] = generator.distribution
            flash(
                f"{generator.distribution['total']} random numbers successfully generated."
            )
            msg = "success"
        else:
            msg = "fail"
            flash("Quantity less than 1 cannot be processed.")

        return render_template(
            "main.html", form=form, header=header, page="main", msg=msg
        )

    return render_template("main.html", form=form, header=header, page="main")


@bp.route("/reset", methods=["POST"])
def reset():
    session.pop("numbers", None)
    session.pop("distribution", None)

    return redirect(url_for("api.main"))
