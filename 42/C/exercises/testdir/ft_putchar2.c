/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar2.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/08 11:12:11 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/08 11:26:29 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putchar (char c);

{

	
	int index;

	index = 0;
	{
		while(index < 10)
		write(1, &c, 1);
		index++;
	}


int main(void)
	{
	write(1, "A", 1);
	return (0);
	}
}
