import pika


def publish_to_queue(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # יצירת תור במידה והוא לא קיים
    channel.queue_declare(queue=queue_name)

    # שליחת ההודעה לתור
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print(f" [x] Sent {message} to {queue_name}")

    connection.close()
