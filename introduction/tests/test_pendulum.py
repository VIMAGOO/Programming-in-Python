import pendulum

now = pendulum.now("Europe/Paris")
print(now)

# Changing timezone
now = now.in_timezone("America/Toronto")
print(now)

# Default support for common datetime formats
now = now.to_iso8601_string()
print(now)

# Shifting
now.add(days=2)
print(now)