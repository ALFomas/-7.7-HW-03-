from django import template
import re


register = template.Library()


@register.filter(name='censor')
def censor(value):
    unwanted_words = [ 'хрен', 'хреновой', 'хреновым', 'охренеть', 'бубен']
    for word in unwanted_words:
        pattern = re.compile(r'(?i)\b' + word + r'\b')
        value = pattern.sub(word[0] + '*'*(len(word)-1), value)
    return value
