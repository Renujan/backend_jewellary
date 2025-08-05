# contact_details/serializers.py
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'Message', 'created_at', 'updated_at']  # Changed 'message' to 'Message'
        read_only_fields = ['id', 'created_at', 'updated_at']