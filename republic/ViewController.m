//
//  ViewController.m
//  republic
//
//  Created by Prabhat Godse on 12/3/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "ViewController.h"

#import <IGListKit/IGListKit.h>
#import "HomeFeedSectionController.h"
#import "ReprHeaderSectionController.h"
#import "ReprDataModel.h"

@interface ViewController () <UITableViewDelegate, UITableViewDataSource, IGListAdapterDelegate> {
    UILabel *label;
    IGListCollectionView *collectionView;
}
@property (nonatomic, strong) IGListAdapter *adapter;
@property (nonatomic, strong) NSArray *objects;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor colorWithWhite:0.85 alpha:1.0];
    label = [[UILabel alloc] initWithFrame:CGRectMake(10, 10, 320, 50)];
    [label setText:@"Know your representative. Location Jersey City, NJ"];
    label.textColor = [UIColor blackColor];
    [self.view addSubview:label];
    
    //Data
    ReprDataModel *mayor = [[ReprDataModel alloc] init];
    mayor.twitter = @"StevenFulop";
    
    ReprDataModel *senD = [[ReprDataModel alloc] init];
    senD.twitter = @"CoreyBooker";
    
    
//    self.objects = @[@"Mayor: Steven Fulop", mayor,
//             @"US Senator: Corey Booker", senD];
    self.objects = @[];
    
    UICollectionViewFlowLayout *layout = [[UICollectionViewFlowLayout alloc] init];
    
    collectionView = [[IGListCollectionView alloc] initWithFrame:CGRectZero
                                            collectionViewLayout:layout];
    collectionView.backgroundColor = [UIColor colorWithWhite:0.76 alpha:1.0];
    [self.view addSubview:collectionView];
    
    _adapter = [[IGListAdapter alloc] initWithUpdater:[[IGListAdapterUpdater alloc] init]
                                       viewController:self
                                     workingRangeSize:0];
    _adapter.collectionView = collectionView;
    _adapter.dataSource = self;
    
    [self getRepresentativesByLocation:@"NJ" type:@"rep"];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
}

- (void)viewDidLayoutSubviews {
    [super viewDidLayoutSubviews];
    CGFloat height = self.view.frame.size.height - label.frame.size.height;
    collectionView.frame = CGRectMake(0, 50, self.view.frame.size.width, height);
    [self.adapter performUpdatesAnimated:YES completion:nil];
}

#pragma mark Web Services

- (void)getRepresentativesByLocation:(NSString*)state type:(NSString*)type {
    NSString *baseUrl = @"http://localhost:8888";
    
    NSString *reprSearchUrl = [NSString stringWithFormat:@"%@/congress?state=%@&congressmen_type=%@",
                               baseUrl, state, type];
    
    NSURL *url = [NSURL URLWithString:reprSearchUrl];
    
    [NSURLConnection sendAsynchronousRequest:[NSURLRequest requestWithURL:url]
                                       queue:[NSOperationQueue mainQueue]
                           completionHandler:^(NSURLResponse * _Nullable response, NSData * _Nullable data, NSError * _Nullable connectionError) {
                               NSInteger statusCode = [(NSHTTPURLResponse *)response statusCode];
                               if (statusCode == 200) {
                                   NSError *parseError = nil;
                                   NSDictionary *dictionary = [NSJSONSerialization JSONObjectWithData:data options:0 error:&parseError];
                                   [self _onReloadReprData:dictionary];
                               }
                           }];
}

- (void)_onReloadReprData:(NSDictionary*)data {
//    if([data class] != [NSArray class]) {
//        return;
//    }
    NSArray *dataList = (NSArray*)data;
    
    NSMutableArray *feedItems = [NSMutableArray array];
    
    for(NSDictionary *item in dataList) {
        NSString *type = [item[@"type"] isEqualToString:@"sen"] ? @"Senator" : @"Congressmen";
        NSString *name = [NSString stringWithFormat:@"%@ %@", item[@"first_name"], item[@"last_name"]];
        NSString *feedTitle = [NSString stringWithFormat:@"US %@: %@", type, name];
        
        [feedItems addObject:feedTitle];
        
        NSDictionary *social = item[@"social_media"];
        ReprDataModel *senD = [[ReprDataModel alloc] init];
        senD.twitter = social[@"twitter"];
        [feedItems addObject:senD];
    }
    
    self.objects = feedItems;
    [_adapter reloadDataWithCompletion:nil];
}

#pragma mark IGListAdapterDataSource

- (NSArray<id <IGListDiffable>> *)objectsForListAdapter:(IGListAdapter *)listAdapter {
    return self.objects;
}

- (IGListSectionController <IGListSectionType> *)listAdapter:(IGListAdapter *)listAdapter
                                  sectionControllerForObject:(id)object {
    if([object isKindOfClass:[NSString class]]) {
        return [[ReprHeaderSectionController alloc] init];
    }

    return [[HomeFeedSectionController alloc] init];
    
}

- (nullable UIView *)emptyViewForListAdapter:(IGListAdapter *)listAdapter {
    return nil;
}

@end
