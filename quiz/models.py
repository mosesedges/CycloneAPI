from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)
    
    
    def __str__(self):
        return self.name
    

class Quizzes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=225, default=_('New Quiz'), verbose_name=_('Quizzes'))
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']
        
        def __str__(self):
            return self.title
        
    
class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Question(Updated):
    SCALE = (
        (0, _('fundermentals')),
        (1, _('biginning')),
        (2, _('intermediate')),
        (3, _('advanced')),
        (4, _('expert'))
    )
    
    TYPE = (
        (0, _('multiple_choices')),
    )
    
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, verbose_name=_('Type of Question'), default=0) 
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    difficulty = models.IntegerField(choices=SCALE, verbose_name=_('Difficulty'), default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))
    
    def __str__(self):
        return self.title
    
    
class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text =models.CharField(max_length=225, verbose_name=_('Answer Text'))
    is_right  = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']
        
        def __str__(self):
            return self.answer_test