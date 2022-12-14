import logging
from collections import namedtuple
from datetime import date

from rest_framework import serializers

from rooms.models import Booking, Room
from users.models import User

Range = namedtuple('Range', ['start', 'end'])

logger = logging.getLogger('logger')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data: dict) -> User:
        user = User(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'number',
            'name',
            'price',
            'capacity',
        ]


class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    requested_room = serializers.IntegerField(write_only=True)
    room = serializers.IntegerField(source='room.number', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'pk',
            'requested_room',
            'room',
            'guest',
            'date_check_in',
            'date_check_out',
        ]

        read_only_fields = ['guest', 'room']

    def validate(self, data: dict) -> dict:
        requested_check_in = data.get('date_check_in')
        requested_check_out = data.get('date_check_out')
        requested_room = data.get('requested_room')
        if not Room.objects.filter(number=requested_room).exists():
            raise serializers.ValidationError(
                f'There is not room with number {requested_room}'
            )
        if requested_check_in < date.today():
            raise serializers.ValidationError(
                'You can\'t book earlier than today'
            )

        if requested_check_in > requested_check_out:
            raise serializers.ValidationError(
                'Check-in date must be earlier than check-out date'
            )
        elif requested_check_in == requested_check_out:
            raise serializers.ValidationError('Select at least one night')
        bookings = Booking.objects.filter(room__number=requested_room)

        for booking in bookings:  # check if requested dates are available
            r1 = Range(booking.date_check_in, booking.date_check_out)
            r2 = Range(requested_check_in, requested_check_out)
            latest_start = max(r1.start, r2.start)
            earliest_end = min(r1.end, r2.end)
            delta = (latest_start - earliest_end).days
            if delta < 0:
                raise serializers.ValidationError(
                    'Sorry, the room is not available for the given dates'
                )
        return data

    def create(self, validated_data: dict) -> Booking:
        user = self.context.get('request').user  # add user from context
        room = validated_data.get('requested_room')
        room = Room.objects.get(number=room)
        requested_check_in = validated_data.get('date_check_in')
        requested_check_out = validated_data.get('date_check_out')
        booking = Booking.objects.create(
            room=room,
            guest=user,
            date_check_in=requested_check_in,
            date_check_out=requested_check_out,
        )
        return booking
