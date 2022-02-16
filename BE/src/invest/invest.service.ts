import { Injectable, Logger } from '@nestjs/common';
import { Item } from './item.model';

@Injectable()
export class InvestService {
  private logger = new Logger('InvestService');
  private items: Item[] = [
    {
      id: 1,
      title: '전북 전주시 덕진구 태양광 발전소 투자',
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
        '국가는 과학기술의 혁신과 정보 및 인력의 개발을 통하여 국민경제의 발전에 노력하여야 한다. 제안된 헌법개정안은 대통령이 20일 이상의 기간 이를 공고하여야 한다. 국회는 국무총리 또는 국무위원의 해임을 대통령에게 건의할 수 있다. 누구든지 체포 또는 구속을 당한 때에는 즉시 변호인의 조력을 받을 권리를 가진다. 다만, 형사피고인이 스스로 변호인을 구할 수 없을 때에는 법률이 정하는 바에 의하여 국가가 변호인을 붙인다.',
    },
  ];

  constructor() {}

  getItem(id: number): Item {
    this.logger.verbose(`return Item: ${id}`);
    const result = this.items.find((item: Item) => item.id === id);
    return result;
  }
}
