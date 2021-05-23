import datetime
import gantt


# Create some tasks

t1 = gantt.Task(name='A', start=datetime.date(2021, 5, 1), duration=1)
t2 = gantt.Task(name='B', start=datetime.date(2021, 5, 2), duration=3)
t3 = gantt.Task(name='C', start=datetime.date(2021, 5, 2), duration=4)
t4 = gantt.Task(name='D', start=datetime.date(2021, 5, 5), duration=7)
t5 = gantt.Task(name='E', start=datetime.date(2021, 5, 11), duration=2)
t6 = gantt.Task(name='F', start=datetime.date(2021, 5, 4), duration=5)
t7 = gantt.Task(name='G', start=datetime.date(2021, 5, 4), duration=2)
t8 = gantt.Task(name='H', start=datetime.date(2021, 5, 4), duration=1)
t9 = gantt.Task(name='I', start=datetime.date(2021, 5, 6), duration=3)
t10 = gantt.Task(name='J', start=datetime.date(2021, 5, 13), duration=1)

t1 = gantt.Task(name='A', start=datetime.date(2021, 5, 1), duration=1, color="#FF8080")
t2 = gantt.Task(name='B', start=datetime.date(2021, 5, 2), duration=3, depends_of=[t1, t4])
t3 = gantt.Task(name='C', start=datetime.date(2021, 5, 2), duration=4, depends_of=[t1, t6, t8], color="#FF8080")
t4 = gantt.Task(name='D', start=datetime.date(2021, 5, 5), duration=7, depends_of=[t2, t5])
t5 = gantt.Task(name='E', start=datetime.date(2021, 5, 11), duration=2, depends_of=[t4, t10])
t6 = gantt.Task(name='F', start=datetime.date(2021, 5, 4), duration=5, depends_of=[t3, t9])
t7 = gantt.Task(name='G', start=datetime.date(2021, 5, 4), duration=2, depends_of=[t3, t9], color="#FF8080")
t8 = gantt.Task(name='H', start=datetime.date(2021, 5, 4), duration=1, depends_of=[t3, t9])
t9 = gantt.Task(name='I', start=datetime.date(2021, 5, 6), duration=3, depends_of=[t6, t7, t8, t10], color="#FF8080")
t10 = gantt.Task(name='J', start=datetime.date(2021, 5, 13), duration=1, depends_of=[t5, t9], color="#FF8080")


# Create a project
p1 = gantt.Project(name='Projekt')

# Add tasks to this project
p1.add_task(t1)
p1.add_task(t2)
p1.add_task(t3)
p1.add_task(t4)
p1.add_task(t5)
p1.add_task(t6)
p1.add_task(t7)
p1.add_task(t8)
p1.add_task(t9)
p1.add_task(t10)

p1.make_svg_for_tasks(filename='test_full.svg', today=datetime.date(2021, 5, 1), start=datetime.date(2021, 5, 1), end=datetime.date(2021, 5, 13))
p1.make_svg_for_tasks(filename='test_full2.svg', today=datetime.date(2021, 5, 1))
p1.make_svg_for_tasks(filename='test.svg', today=datetime.date(2021, 5, 1), start=datetime.date(2021, 5, 1), end=datetime.date(2021, 5, 13))
p1.make_svg_for_tasks(filename='test_weekly.svg', today=datetime.date(2021, 5, 1), scale=gantt.DRAW_WITH_WEEKLY_SCALE)