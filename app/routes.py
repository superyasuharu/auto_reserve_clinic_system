from typing import Any

from flask import redirect, render_template, request, url_for

from app import app, db
from app.database_manager.manege_db import add_row_to_table, delete_row_from_table
from app.database_manager.util import convert_str_to_datatime
from app.models.clinic_info import OmoriHihuka, OmoriJibika
from app.models.registed_clinic import RegistedClinic
from app.models.reserve_info import ReserveInfo
from app.models.user import User


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/submit-reservation", methods=["POST"])
def submit_reservation() -> Any:
    clinic: str | None = request.form.get("clinic")
    patient: str | None = request.form.get("patient")
    reservation_date: str | None = request.form.get("reservation-date")
    hours: str | None = request.form.get("hours")
    minutes: str | None = request.form.get("minutes")

    reserve_time = convert_str_to_datatime(
        reservation_date=reservation_date, hours=hours, minutes=minutes
    )

    add_row_to_table(
        db,
        ReserveInfo,
        reserve_clinic=clinic,
        patient_name=patient,
        reserve_time=reserve_time,
    )

    return redirect(
        url_for(
            "confirmation",
            clinic=clinic,
            patient_name=patient,
            appointment_date=reservation_date,
            appointment_time=f"{int(hours):02}:{int(minutes):02}",
        )
    )


@app.route("/confirmation")
def confirmation() -> str:
    clinic = request.args.get("clinic")
    patient_name = request.args.get("patient_name")
    appointment_date = request.args.get("appointment_date")
    appointment_time = request.args.get("appointment_time")
    return render_template(
        "confirmation.html",
        clinic=clinic,
        patient_name=patient_name,
        appointment_date=appointment_date,
        appointment_time=appointment_time,
    )


@app.route("/view_applications")
def view_applications() -> str:
    reserve_infos = ReserveInfo.query.all()

    return render_template("applications.html", reserve_infos=reserve_infos)


@app.route("/delete/<int:id>")
def delete(id: int) -> Any:
    delete_row_from_table(db, ReserveInfo, id=id)
    return redirect(url_for("view_applications"))


@app.route("/clinic_regist_info", methods=["GET", "POST"])
def clinic_regist_info() -> str:
    if request.method == "POST":
        clinic_id = request.form.get("clinic_id")
    elif request.method == "GET":
        clinic_id = request.args.get("clinic_id", "1")
    if clinic_id == "1":
        clinic_table = OmoriJibika
    elif clinic_id == "2":
        clinic_table = OmoriHihuka
    else:
        raise ValueError(f"Invalid table name: {clinic_id}")
    if request.method == "POST":
        patient_name = request.form["patient_name"]
        patient_id_in_clinic = request.form["patient_id_in_clinic"]
        password_in_clinic = request.form["password_in_clinic"]
        add_row_to_table(
            db,
            clinic_table,
            patient_name=patient_name,
            patient_id_in_clinic=patient_id_in_clinic,
            password_in_clinic=password_in_clinic,
        )

    all_clinics = RegistedClinic.query.all()

    patient_infos = clinic_table.query.all()
    return render_template(
        "clinic_regist_info.html",
        all_clinics=all_clinics,
        patient_infos=patient_infos,
        clinic_id=clinic_id,
    )
