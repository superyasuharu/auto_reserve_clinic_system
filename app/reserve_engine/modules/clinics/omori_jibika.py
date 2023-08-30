from selenium.webdriver.common.by import By

from ..util import BaseClinicReservation, BaseScraping, PatientInfo, ReserveTime


class PatientInfoInput(BaseScraping):
    def input_patient_info(self, patient_info: PatientInfo) -> None:
        self.driver.find_element(By.ID, "c_code").send_keys(patient_info.patient_number)
        self.driver.find_element(By.ID, "c_pass").send_keys(patient_info.password)
        self.driver.find_element(By.NAME, "bOK").click()


class AmPmSelection(BaseScraping):
    def is_am(self, hour_value: int) -> bool:
        pm_start_time = 13
        return hour_value < pm_start_time

    def select_ampm(self, reserve_time: ReserveTime) -> None:
        ampm_elements = self.driver.find_elements(By.CLASS_NAME, "date")
        am_pm_text = "午前" if self.is_am(reserve_time.hour) else "午後"
        is_correct_input = False
        for element in ampm_elements:
            if am_pm_text in element.text:
                element.click()
                is_correct_input = True
                break

        if not is_correct_input:
            raise ValueError(f"Invalid input: {reserve_time.hour} {reserve_time.min}")


class PersonNumSelection(BaseScraping):
    def select_person_num(self, patient_infos: list[PatientInfo]) -> None:
        person_num = len(patient_infos)
        person_num_elements = self.driver.find_elements(By.CLASS_NAME, "date")
        person_num_elements[person_num - 1].click()


class TimeSelection(BaseScraping):
    def _get_time_text(self, reserve_time: ReserveTime) -> str:
        time_text = f"{reserve_time.hour}:{reserve_time.min:02}"
        return time_text

    def select_time(self, reserve_time: ReserveTime) -> None:
        time_elements = self.driver.find_elements(By.CLASS_NAME, "date")
        time_text = self._get_time_text(reserve_time)
        for time_element in time_elements:
            if time_element.text == time_text:
                time_element.click()
                break


class OmoriJibikaReservation(BaseClinicReservation):
    def __init__(self) -> None:
        clinic_url = "https://ssc6.doctorqube.com/omori-jibika/input.cgi?vMode=mode_book&stamp=863147"
        super().__init__(clinic_url=clinic_url)

    def make_reservation(
        self, patient_infos: list[PatientInfo], reserve_time: ReserveTime
    ) -> None:
        patient_info_inputter = PatientInfoInput(self.driver)

        patient_info_inputter.input_patient_info(patient_infos[0])
        AmPmSelection(self.driver).select_ampm(reserve_time)
        PersonNumSelection(self.driver).select_person_num(patient_infos)
        for person_idx, patient_info in enumerate(patient_infos):
            if person_idx == 0:
                continue
            patient_info_inputter.input_patient_info(patient_info)
        TimeSelection(self.driver).select_time(reserve_time)
