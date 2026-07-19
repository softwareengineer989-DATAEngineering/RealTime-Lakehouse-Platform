# Kafka Topic Design

## Purpose

Defines the enterprise messaging topology.

## Topics

orders.raw

orders.validated

orders.deadletter

customers.raw

inventory.events

platform.audit

## Design Principles

- Raw events never modified

- Validation isolated

- DLQ separated

- Audit topic retained

- Parallel processing enabled through partitioning