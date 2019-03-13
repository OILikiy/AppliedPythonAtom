#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts = {}
        self.users = {}
        # raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        self.posts[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.posts:
            if user_id not in self.posts[post_id][1]:
                self.posts[post_id][1].append(user_id)
        else:
            self.posts[post_id] = [[], [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.users:
            self.users[follower_user_id] = [followee_user_id]
        else:
            self.users[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        list_of_posts_for_users_id = [key for key in self.posts.keys()
                                      if self.posts[key][0]
                                      in self.users[user_id]]
        print("recent: ", sorted(list_of_posts_for_users_id, reverse=True)[:k])
        return sorted(list_of_posts_for_users_id, reverse=True)[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        list_of_posts = [post for post in self.posts]
        list_of_posts_sorted_by_key = sorted(list_of_posts,
                                             key=lambda post_id: post_id,
                                             reverse=True)
        list_of_posts_sorted_by_popular = sorted(list_of_posts_sorted_by_key,
                                                 key=lambda i:
                                                 len(self.posts[i][1]),
                                                 reverse=True)
        return list_of_posts_sorted_by_popular[:k]
