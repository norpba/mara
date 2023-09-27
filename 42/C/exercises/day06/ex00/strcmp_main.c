/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strcmp_main.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/06 20:03:31 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/06 21:22:16 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h> // CAREFUL!!!!!!!!!!!!!!!

int ft_strcmp(char *s1, char *s2);

int main(void)
{
	char s1[] = "aac";
	char s2[] = "aaaaa";

	int result;

	result = ft_strcmp(s1, s2);
	printf("The result is %d\n", result);

	return (0);
}
