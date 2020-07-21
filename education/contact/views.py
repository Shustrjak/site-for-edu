from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import FeedbackForm
from rq.decorators import job
from redis import Redis
from education.passmail import email  # инструкция в settings.py

# queue = Queue(connection=Redis())
@job("default", connection=Redis())
def contact_view(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            input_name = form.cleaned_data['input_name']
            input_mail = form.cleaned_data['input_mail']
            input_text = form.cleaned_data['input_text']
            copy = form.cleaned_data['copy']

            recipients = [email]

            if copy:
                recipients.append(input_mail)
            try:
                send_mail(input_name, input_text, email, recipients)
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return render(request, 'contact/thanks.html')
    else:

        form = FeedbackForm()

    return render(request, 'contact/contact.html', {'form': form})


# job = queue.enqueue(contact_view, 'contact/contact.html')
print(job)
