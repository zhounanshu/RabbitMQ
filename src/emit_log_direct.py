import pika
import sys

connection = pika.BlockingConnection(
									pika.BlockingConnectionParameters(
									host = 'localhost'))

channel.exchange_declare(exchange = 'direct_logs', 
						type = 'direct') 
serverity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ''.join(sys.argv[2:]) or 'hello world!'
channel.basic_publish(exchange = 'direct_logs', 
					  routing_key = serverity, 
					  body = message)
print '[x] sent %r'%(serverity, message)
connection.close()