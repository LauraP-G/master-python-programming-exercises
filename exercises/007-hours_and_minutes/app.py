def hours_minutes(seconds):
  # Your code here
  paso_a_horas = round(seconds / 3600)
  intermedio = seconds%3600
  paso_a_minutos = intermedio / 60
  return paso_a_horas, paso_a_minutos
# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
