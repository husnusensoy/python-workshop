#  Student Exam Details

Email to our dean

## {{ test_name|title }} Scores

Here are the scores of our studeunts for this exam order by fails first

{% for stu in students|sort(attribute="score") %}
* **Student**: {{ stu.name }}
  * **Score**: {{ stu.score }} out of {{ max_score }}
  {% if stu.score > 80 %}
  * **PASS**: yes
  {% else -%}
  * **PASS**: no
  {% endif %}
{% endfor %}

