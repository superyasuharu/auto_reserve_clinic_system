from modules.clinics.omori_jibika import OmoriJibikaReservation
from modules.util import PatientInfo, ReserveTime

if __name__ == "__main__":
    patient_infos = [PatientInfo("0010841", "0829")]
    reserve_time = ReserveTime(15, 0)
    reservation = OmoriJibikaReservation()
    reservation.make_reservation(patient_infos=patient_infos, reserve_time=reserve_time)
    reservation.close()
