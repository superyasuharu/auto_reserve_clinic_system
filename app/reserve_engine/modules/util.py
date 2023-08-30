from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from selenium.webdriver import Chrome


@dataclass
class PatientInfo:
    patient_number: str
    password: str


@dataclass
class ReserveTime:
    year: int
    month: int
    day: int
    hour: int
    min: int


@dataclass
class ReserveInfo:
    clinic: str
    patient_name: str
    reserve_time: ReserveTime


class BaseScraping:
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver


class BaseClinicReservation(metaclass=ABCMeta):
    def __init__(self, clinic_url: str) -> None:
        self.driver: Chrome = Chrome()
        self.driver.get(clinic_url)

    @abstractmethod
    def make_reservation(
        self, patient_infos: list[PatientInfo], reserve_time: ReserveTime
    ) -> None:
        pass

    def close(self) -> None:
        self.driver.quit()
