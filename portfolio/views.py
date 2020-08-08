from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


def resume(request):

    # *  All Profile objects
    profile = Profile.objects.get(full_name='Dmytro Tkach')
    print(profile.profile_img.url)
    print(profile.project_set.all().first())
    print(profile.project_set.all()[0])
    print(profile.project_set.all().get(title='Todo - App'))
    print(profile.about_set.all().filter(hidden=False))
    print(profile.about_set.all().filter(hidden=True))
    print(profile.achievement_set.all().first().slug)

    # * Profile skills
    skills = []
    num_skills = profile.expertise_set.all()[0].skills.all().count()
    for skill in range(num_skills):
        skills.append(profile.expertise_set.all()[0].skills.all()[skill])
    
    if num_skills % 2 == 0:
        num_left_skills = int(num_skills / 2)
    else:
        num_left_skills = int(num_skills / 2) + 1


    context = {
        'profile': profile,
        'left_skills': skills[0 : num_left_skills],
        'right_skills': skills[num_left_skills : num_skills]
    }

    # * Get in touch - mail sending
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_subject = request.POST['message-subject']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send a confirmation email to the client
        try:
            send_mail(
                'Confirmation email - Dmytro Tkach',
                f'''
                Hi, {message_name}!

                Thank's for your email,
                I'll contac you as soon as possible.

                __
                Dmytro Tkach
                ''',
                settings.EMAIL_HOST_USER,
                [message_email],
                fail_silently=False
            )
        except:
            context_b = {
                'message_name': 'Your email is invalid, please try again!',
                'color':'red'
            }
            context.update(context_b)
            return render(request, 'portfolio/resume.html', context)

        # send an email to me 
        send_mail(
            message_subject,
            f'''
            {message}
            __
            from: {message_name}
            email - {message_email}
            ''',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False
        )
        
        context_c = {
            'message_name': f"{message_name} a confirmation mail was sended at this address:",
            'message_email': message_email,
            'color':'green',
            'check_mail': f"If you haven't received it, try again and check your insert mail",
            'color_chek': 'red'
        }

        context.update(context_c)

        return render(request, 'portfolio/resume.html', context )
    
    else:
        return render(request, 'portfolio/resume.html', context)