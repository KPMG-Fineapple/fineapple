import { Controller, Get, Logger, Query } from '@nestjs/common';
import { ConsumptionService } from './consumption.service';

@Controller('/predict/consumption')
export class ConsumptionController {
  private logger = new Logger('ConsumptionController');
  constructor(private consumptionService: ConsumptionService) {}

  @Get()
  getConsumption(@Query('address') address: string) {
    this.logger.verbose(`address: ${address} trying to get consumption`);
    return this.consumptionService.getConsumption(address);
  }
}
