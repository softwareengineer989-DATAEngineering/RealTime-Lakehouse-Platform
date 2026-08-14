"""
Backward compatibility module.

Future producer creation should use:

ProducerFactory
ProducerService
"""

from retaillake.kafka.producer.producer_factory import ProducerFactory

producer = ProducerFactory.create()