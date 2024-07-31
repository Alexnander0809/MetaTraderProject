import { TestBed } from '@angular/core/testing';

import { MetaTraderService } from './meta-trader.service';

describe('MetaTraderService', () => {
  let service: MetaTraderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MetaTraderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
