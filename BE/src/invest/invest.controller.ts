import { Controller, Get, Logger, Param, ParseIntPipe } from '@nestjs/common';
import { InvestService } from './invest.service';
import { Item } from './item.model';

@Controller('invest')
export class InvestController {
  private logger = new Logger('InvestController');
  constructor(private investService: InvestService) {}

  @Get('/items/:id')
  getItem(@Param('id', ParseIntPipe) id: number): Item {
    this.logger.verbose(`Item ${id} trying to get all boards`);
    return this.investService.getItem(id);
  }
}
