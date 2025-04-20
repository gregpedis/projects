#!/bin/bash
rm dnd10k.db && sqlite3 dnd10k.db < initialize_db.sql
