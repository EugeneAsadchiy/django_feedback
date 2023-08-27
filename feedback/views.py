from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import ListView, DetailView


class FeedBackView(CreateView):
    model = Feedback
    # fields = ["name", "surname"]  # либо "__all__"
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = "/done"


# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, "feedback/load_file.html", context={"form": form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect("/done")
#         return render(request, "feedback/load_file.html", context={"form": form})
#

# class FeedBackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/load_file.html'
#     success_url = "/done"
#
#     def form_valid(self, form):
#         form.save()
#         return super(FeedBackView, self).form_valid(form)

class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback/feedback.html"
    success_url = "/done"

# class FeedBackUpdateView(View):
#     def get(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=feed)
#         return render(request, 'feedback/load_file.html', context={'form': form})
#
#     def post(self, request, id_feedback):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/done')
#         return render(request, "feedback/load_file.html", context={"form": form})


class DoneView(TemplateView):
    template_name = "feedback/done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context["name"] = "Ivanov I.I."
        context["date"] = "26.12.2002"
        return context


# class ListFeedBack(TemplateView):
#     template_name = "feedback/list_feedback.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedbacks'] = Feedback.objects.all()
#         return context

class ListFeedBack(ListView):
    template_name = "feedback/list_feedback.html"
    model = Feedback  # само выберет все данные и передаст в контекст
    context_object_name = "feedbacks"

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3) #пример
        return queryset


# class DetailFeedBack(TemplateView):
#     template_name = "feedback/detail_feedback.html"
#
#     def get_context_data(self, **kwargs):
#         # kwargs.id_feedback
#         context = super().get_context_data(**kwargs)
#         context['detail_feedback'] = Feedback.objects.get(id=kwargs["id_feedback"])
#         return context

class DetailFeedBack(DetailView):
    template_name = "feedback/detail_feedback.html"
    model = Feedback
    context_object_name = "detail_feedback"
