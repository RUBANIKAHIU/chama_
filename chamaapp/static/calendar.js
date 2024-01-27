const calendar = document.getElementById('calendar');
const modal = document.getElementById('modal');
const monthYearElement = document.getElementById('month-year');

let selectedDate = new Date();

function generateCalendar() {
    const daysInMonth = new Date(selectedDate.getFullYear(), selectedDate.getMonth() + 1, 0).getDate();

    monthYearElement.textContent = `${getMonthName(selectedDate.getMonth())} ${selectedDate.getFullYear()}`;

    for (let i = 1; i <= daysInMonth; i++) {
        const dayElement = document.createElement('div');
        dayElement.classList.add('day');
        dayElement.textContent = i;

        dayElement.addEventListener('click', () => {
            selectedDate = new Date(selectedDate.getFullYear(), selectedDate.getMonth(), i);
            openModal();
        });

        calendar.appendChild(dayElement);
    }
}

function prevMonth() {
    selectedDate.setMonth(selectedDate.getMonth() - 1);
    updateCalendar();
}

function nextMonth() {
    selectedDate.setMonth(selectedDate.getMonth() + 1);
    updateCalendar();
}

function updateCalendar() {
    // Remove existing calendar content
    calendar.innerHTML = '';

    generateCalendar();
}

function openModal() {
    modal.style.display = 'block';
    const titleInput = document.getElementById('meetingTitle');
    const descriptionInput = document.getElementById('meetingDescription');
    const dateInput = document.getElementById('meetingDate');

    titleInput.value = '';
    descriptionInput.value = '';
    dateInput.valueAsDate = selectedDate;

    // Clear previous event listeners to avoid duplicates
    document.getElementById('saveMeetingBtn').removeEventListener('click', saveMeeting);
    document.getElementById('removeMeetingBtn').removeEventListener('click', removeMeeting);

    // Add event listener for saving a meeting
    document.getElementById('saveMeetingBtn').addEventListener('click', saveMeeting);

    // Add event listener for removing a meeting
    document.getElementById('removeMeetingBtn').addEventListener('click', removeMeeting);
}

function closeModal() {
    modal.style.display = 'none';
}

function saveMeeting() {
    const title = document.getElementById('meetingTitle').value;
    const description = document.getElementById('meetingDescription').value;
    const date = document.getElementById('meetingDate').valueAsDate;

    if (title.trim() === '' || description.trim() === '' || !date) {
        alert('Please enter title, description, and date for the meeting.');
        return;
    }

    const meetingElement = document.createElement('div');
    meetingElement.classList.add('meeting');
    meetingElement.innerHTML = `<span onclick="editMeeting(this)">✎</span> <strong>${title}</strong><br>${description}`;

    const dayElement = calendar.children[selectedDate.getDate() - 1];
    dayElement.appendChild(meetingElement);

    closeModal();
}

function removeMeeting() {
    const dayElement = calendar.children[selectedDate.getDate() - 1];
    const meetings = dayElement.getElementsByClassName('meeting');

    for (const meeting of meetings) {
        meeting.addEventListener('click', (event) => {
            event.stopPropagation(); // Prevent clicking on the day element
        });

        meeting.classList.add('removable');
        meeting.innerHTML += ' <span onclick="confirmRemoveMeeting(this)">❌</span>';
    }

    closeModal();
}

function confirmRemoveMeeting(element) {
    const meeting = element.parentElement;
    const dayElement = meeting.parentElement;

    dayElement.removeChild(meeting);
}

function editMeeting(element) {
    const meeting = element.parentElement;
    const dayElement = meeting.parentElement;

    document.getElementById('meetingTitle').value = meeting.querySelector('strong').textContent;
    document.getElementById('meetingDescription').value = meeting.innerHTML.split('<br>')[1];
    document.getElementById('meetingDate').valueAsDate = selectedDate;

    dayElement.removeChild(meeting);
    closeModal();
}

function formatDate(date) {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

function getMonthName(monthIndex) {
    const monthNames = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ];

    return monthNames[monthIndex];
}

generateCalendar();
