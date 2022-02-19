import { Controller, Get, Logger, Param, ParseIntPipe } from '@nestjs/common';
import { InvestService } from './invest.service';
import { Item } from './item.model';

@Controller('invest')
export class InvestController {
  private logger = new Logger('InvestController');
  constructor(private investService: InvestService) {}

  @Get('/items')
  getAllItem(): Item[] {
    this.logger.verbose(`trying to get All Item`);
    return this.investService.getAllItem();
  }

  @Get('/items/:id')
  getItem(@Param('id', ParseIntPipe) id: number): Item {
    this.logger.verbose(`Item ${id} trying to get Item`);
    return this.investService.getItem(id);
  }
}
