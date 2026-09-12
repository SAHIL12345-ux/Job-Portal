from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import application, job
from .forms import jobForm

def home(request):
    return render(request, 'home.html')

class jobListView(ListView):
    model = job
    template_name = 'jobs/job_list.html'
    context_object_name = 'all_jobs'


class jobDetailView(DetailView):
    model = job
    template_name = 'jobs/job_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['already_applied'] = application.objects.filter(
                job=self.object,
                applicant=self.request.user
            ).exists()

        return context


class jobCreateView(LoginRequiredMixin, CreateView):
    model = job
    form_class = jobForm
    template_name = 'job_form.html'
    success_url = reverse_lazy('job_list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class jobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = job
    form_class = jobForm
    template_name = 'job_form.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        return self.get_object().posted_by == self.request.user


class jobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        return self.get_object().posted_by == self.request.user


class myJobListView(LoginRequiredMixin, ListView):
    model = job
    template_name = 'jobs/my_jobs.html'
    context_object_name = 'my_jobs'

    def get_queryset(self):
        return job.objects.filter(posted_by=self.request.user)
    
@login_required
def apply_to_job(request, pk):
    job_obj = get_object_or_404(job, pk=pk)

    if application.objects.filter(
        job=job_obj,
        applicant=request.user
    ).exists():
        return redirect('job_detail', pk=pk)

    application.objects.create(
        job=job_obj,
        applicant=request.user
    )

    return redirect('job_detail', pk=pk)
class myApplicationsListView(LoginRequiredMixin, ListView):
    model = application
    template_name = 'jobs/my_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return application.objects.filter(
            applicant=self.request.user
        )