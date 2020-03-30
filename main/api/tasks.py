from api.rki import process_data
from background_task.models import Task


process_data(repeat=Task.DAILY)
