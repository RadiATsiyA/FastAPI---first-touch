from fastapi import status, HTTPException


UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid email or password"
)


TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired"
)


TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token doesn't exists"
)


InvalidTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token format"
)


UserIsNotExistsException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


RoomCannotBeBookedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Room can not be booked"
)


HotelAddingErrorException = HTTPException(
    status_code=status.HTTP_406_NOT_ACCEPTABLE,
    detail="Something went wrong"
)


UserIsNotAuthorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="You have to be logged in to add hotel"
)


HotelUpdateErrorExecption = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Error while updating hotel"
)





