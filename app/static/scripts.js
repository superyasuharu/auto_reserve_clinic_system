// let clinicsData = [];
let clinicsData = [
    {
      "id": "1",
      "name": "大森耳鼻咽喉科",
      "morning": {
          "startTime": { "hour": 9, "minute": 0 },
          "endTime": { "hour": 13, "minute": 0 }
        },
      "afternoon": {
          "startTime": { "hour": 15, "minute": 0 },
          "endTime": { "hour": 18, "minute": 0 }
        },
      "interval": 10,
      "patients": [
        { "id": "patient1", "name": "ゆうせい" },
        { "id": "patient2", "name": "はるあき" },
        { "id": "patient3", "name": "やすはる" },
        { "id": "patient4", "name": "かな" },
      ]
    },
    {
      "id": "2",
      "name": "大森皮膚科クリニック",
      "morning": {
          "startTime": { "hour": 9, "minute": 30 },
          "endTime": { "hour": 12, "minute": 30 }
        },
        "afternoon": {
          "startTime": { "hour": 14, "minute": 30 },
          "endTime": { "hour": 18, "minute": 30 }
        },
      "interval": 15,
      "patients": [
          { "id": "patient4", "name": "かな" },
              ]
    }
  ]


  document.addEventListener("DOMContentLoaded", function() {
    const clinicSelect = document.getElementById('clinic');

    // クリニックの選択肢を初期化
    populateClinicsOptions();

    clinicSelect.addEventListener('change', function() {
      updateForSelectedClinic();
    });

    // 最初のクリニックのデータをもとに患者と時間の選択肢を初期化
    updateForSelectedClinic();
  });

  document.addEventListener("DOMContentLoaded", function() {
    const today = new Date();
    const formattedDate = today.toISOString().split('T')[0];
    document.getElementById('reservation-date').value = formattedDate;
});

  function updateForSelectedClinic() {
    const selectedClinicId = document.getElementById('clinic').value;
    const selectedClinic = clinicsData.find(clinic => clinic.id === selectedClinicId);
    populatePatientsOptions(selectedClinic);
    populateTimeOptions(selectedClinic);
  }


  function populateClinicsOptions() {
    const clinicSelect = document.getElementById('clinic');
    clinicsData.forEach(clinic => {
      const option = document.createElement('option');
      option.value = clinic.id;
      option.textContent = clinic.name;
      clinicSelect.appendChild(option);
    });
  }

  function getTimeSlots(session, interval) {
    let currentTime = { hour: session.startTime.hour, minute: session.startTime.minute };
    const slots = [];

    while (currentTime.hour < session.endTime.hour || (currentTime.hour === session.endTime.hour && currentTime.minute < session.endTime.minute)) {
      slots.push({ hour: currentTime.hour, minute: currentTime.minute });
      currentTime.minute += interval;
    // currentTime.minute += 10;

      if (currentTime.minute === 60) {
        currentTime.minute = 0;
        currentTime.hour += 1;
      }
    }

    return slots;
  }

  function populateTimeOptions(clinicData) {
    const hoursSelect = document.getElementById('hours');
    const minutesSelect = document.getElementById('minutes');

    // 既存の選択肢をクリア
    hoursSelect.innerHTML = '';
    minutesSelect.innerHTML = '';

    const morningSlots = getTimeSlots(clinicData.morning, clinicData.interval);
    const afternoonSlots = getTimeSlots(clinicData.afternoon, clinicData.interval);
    const timeSlots = [...morningSlots, ...afternoonSlots];

    timeSlots.forEach(slot => {
      if (!document.querySelector(`#hours option[value="${slot.hour}"]`)) {
        const hourOption = document.createElement('option');
        hourOption.value = slot.hour;
        hourOption.textContent = slot.hour + "時";
        hoursSelect.appendChild(hourOption);
      }
    });

    updateMinuteOptions(timeSlots, hoursSelect.value);

    // 時間が変更された場合、分の選択肢を更新
    hoursSelect.addEventListener('change', () => {
      updateMinuteOptions(timeSlots, hoursSelect.value);
    });
  }

  function updateMinuteOptions(timeSlots, selectedHour) {
    const minutesSelect = document.getElementById('minutes');
    minutesSelect.innerHTML = '';

    timeSlots.forEach(slot => {
      if (slot.hour == selectedHour) {
        const minuteOption = document.createElement('option');
        minuteOption.value = slot.minute;
        minuteOption.textContent = slot.minute + "分";
        minutesSelect.appendChild(minuteOption);
      }
    });
  }

  function populatePatientsOptions(clinicData) {
    const patientSelect = document.getElementById('patient');
    // 既存の選択肢をクリア
    patientSelect.innerHTML = '';

    clinicData.patients.forEach(patient => {
      const option = document.createElement('option');
      option.value = patient.id;
      option.textContent = patient.name;
      patientSelect.appendChild(option);
    });
  }
