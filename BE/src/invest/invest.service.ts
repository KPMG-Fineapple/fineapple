import { Injectable, Logger } from '@nestjs/common';
import { Item } from './item.model';

const yieldData = [
  {
    name: '2월',
    수익률: 5,
  },
  {
    name: '3월',
    수익률: 6,
  },
  {
    name: '4월',
    수익률: 7,
  },
  {
    name: '5월',
    수익률: 8,
  },
  {
    name: '6월',
    수익률: 9,
  },
  {
    name: '7월',
    수익률: 10,
  },
  {
    name: '8월',
    수익률: 11,
  },
  {
    name: '9월',
    수익률: 13,
  },
  {
    name: '10월',
    수익률: 14,
  },
  {
    name: '11월',
    수익률: 15,
  },
  {
    name: '12월',
    수익률: 16,
  },
  {
    name: '1월',
    수익률: 22,
  },
];

@Injectable()
export class InvestService {
  private logger = new Logger('InvestService');
  private items: Item[] = [
    {
      id: 1,
      title: '김해 K 발전소',
      imageUrl: '/static/images/items/item1.jpeg',
      price: 58800,
      investAmount: 120302900,
      investorNumber: 2067,
      companyInfo: {
        name: '주식회사 시티파이브',
        satisfaction: 4,
        investAmount: 700000000,
        investorNumber: 10646,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 5.6,
      profitPercent: 17.4,
      fundingPercent: 23,
    },
    {
      id: 2,
      title: '통영 B 발전소',
      imageUrl: '/static/images/items/item2.jpeg',
      price: 8800,
      investAmount: 10302900,
      investorNumber: 19067,
      companyInfo: {
        name: '주식회사 파인',
        satisfaction: 4.5,
        investAmount: 50000000,
        investorNumber: 57777,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 4.8,
      profitPercent: 24.6,
      fundingPercent: 23,
    },
    {
      id: 3,
      title: '평창 V 발전소',
      imageUrl: '/static/images/items/item3.png',
      price: 58800,
      investAmount: 120302900,
      investorNumber: 2067,
      companyInfo: {
        name: '주식회사 애플',
        satisfaction: 4,
        investAmount: 700000000,
        investorNumber: 10646,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 7.1,
      profitPercent: 32.1,
      fundingPercent: 23,
    },
    {
      id: 4,
      title: '나주 T 발전소',
      imageUrl: '/static/images/items/item4.jpeg',
      price: 58800,
      investAmount: 120302900,
      investorNumber: 2067,
      companyInfo: {
        name: '주식회사 K',
        satisfaction: 4,
        investAmount: 700000000,
        investorNumber: 10646,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 2.7,
      profitPercent: 28.4,
      fundingPercent: 36,
    },
    {
      id: 5,
      title: '제주 A 발전소',
      imageUrl: '/static/images/items/item5.jpeg',
      price: 58800,
      investAmount: 120302900,
      investorNumber: 2067,
      companyInfo: {
        name: '주식회사 P',
        satisfaction: 4,
        investAmount: 700000000,
        investorNumber: 10646,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 6.9,
      profitPercent: 19.2,
      fundingPercent: 57,
    },
    {
      id: 6,
      title: '고리 B 발전소',
      imageUrl: '/static/images/items/item6.jpeg',
      price: 58800,
      investAmount: 120302900,
      investorNumber: 2067,
      companyInfo: {
        name: '주식회사 M>',
        satisfaction: 4,
        investAmount: 700000000,
        investorNumber: 10646,
      },
      description:
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다.',
      yield: yieldData,
      totalFund: 10.2,
      profitPercent: 23.5,
      fundingPercent: 83,
    },
  ];

  getAllItem(): Item[] {
    return this.items;
  }

  getItem(id: number): Item {
    this.logger.verbose(`return Item: ${id}`);
    const result = this.items.find((item: Item) => item.id === id);
    return result;
  }
}
