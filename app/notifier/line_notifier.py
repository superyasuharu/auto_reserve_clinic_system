import requests

from app.reserve_engine.util import PatientInfo, ReserveTime


class LineNotifier:
    def send_line_notify(self, notification_message: str) -> None:
        """
        LINEに通知する
        """
        line_notify_token = "ここに発行したトークン"
        line_notify_api = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {line_notify_token}"}
        data = {"message": f"message: {notification_message}"}
        requests.post(line_notify_api, headers=headers, data=data)
