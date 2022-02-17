import { Test, TestingModule } from '@nestjs/testing';
import { InvestService } from './invest.service';
import { Item } from './item.model';

describe('InvestService', () => {
  let service: InvestService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [InvestService],
    }).compile();

    service = module.get<InvestService>(InvestService);
  });

  describe('GET getItem', () => {
    it('should be defined getItem', () => {
      expect(service.getItem).toBeDefined();
    });

    it('should return Item', () => {
      const item: Item = service.getItem(1);
      console.log(item);
      expect(item.id).toBe(1);
      expect(item.title).toEqual('전북 전주시 덕진구 태양광 발전소 투자');
      expect(typeof item.price).toBe('number');
    });
  });
});
