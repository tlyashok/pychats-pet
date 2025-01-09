from uuid import UUID
from src.domain.aggregated_roots.user_root import UserRoot
from src.domain.exceptions.user_exceptions import UserNotFoundException, UserAlreadyExistsException


class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username: str, full_name: str) -> UserRoot:
        # Проверяем, существует ли уже пользователь с таким именем
        if self.user_repository.get_by_username(username) is not None:
            raise UserAlreadyExistsException(f"User with username '{username}' already exists.")

        # Создаем новый агрегат
        user_root = UserRoot(username=username, full_name=full_name)
        self.user_repository.save(user_root)
        return user_root

    def get_user_by_uuid(self, user_uuid: UUID) -> UserRoot:
        # Получаем пользователя по UUID
        user_root = self.user_repository.get(user_uuid)
        if not user_root:
            raise UserNotFoundException(f"User with UUID '{user_uuid}' not found.")
        return user_root

    def update_user(self, user_uuid: UUID, new_full_name: str) -> UserRoot:
        # Получаем и обновляем пользователя
        user_root = self.get_user_by_uuid(user_uuid)
        user_root.user.full_name = new_full_name
        self.user_repository.save(user_root)
        return user_root

    def change_user_role(self, user_uuid: UUID, new_role: str) -> UserRoot:
        # Логика для изменения роли пользователя
        user_root = self.get_user_by_uuid(user_uuid)
        user_root.user.role = new_role
        self.user_repository.save(user_root)
        return user_root

    def remove_user(self, user_uuid: UUID) -> None:
        # Удаление пользователя
        user_root = self.get_user_by_uuid(user_uuid)
        self.user_repository.remove(user_uuid)
